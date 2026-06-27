resource "azurerm_container_app" "app" {
  name                         = var.container_app_name
  resource_group_name          = azurerm_resource_group.rg.name
  container_app_environment_id = azurerm_container_app_environment.env.id
  revision_mode                = "Single"

  # System Assigned Managed Identity — no username/password for ACR
  identity {
    type = "SystemAssigned"
  }

  registry {
    server   = azurerm_container_registry.acr.login_server
    identity = "System"
  }

  ingress {
    external_enabled = true
    transport        = "http"
    target_port      = 8000

    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }

  template {
    min_replicas = 0
    max_replicas = 1

    container {
      name   = var.container_app_name
      image  = "${azurerm_container_registry.acr.login_server}/${var.docker_image}:${var.docker_tag}"
      cpu    = 0.25
      memory = "0.5Gi"

      env {
        name  = "PORT"
        value = "8000"
      }
    }
  }

  # Depends on role assignment so the identity has AcrPull before first deploy
  depends_on = [azurerm_role_assignment.acr_pull]
}
