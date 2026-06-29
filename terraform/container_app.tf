resource "azurerm_container_app" "app" {
  name                         = var.container_app_name
  resource_group_name          = azurerm_resource_group.rg.name
  container_app_environment_id = azurerm_container_app_environment.env.id
  revision_mode                = "Single"


  secret {
    name  = "client-secret"
    value = var.client_secret
  }

  ingress {
    external_enabled = true
    transport        = "http"
    target_port      = 8002

    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }

  template {
    min_replicas = 1
    max_replicas = 1

    container {
      name   = var.container_app_name
      image = "docker.io/pchelkovskiy/resortsweatherapi-api:latest"
      cpu    = 0.25
      memory = "0.5Gi"

      env {
        name  = "PORT"
        value = "8002"
      }
      env {
        name  = "TENANT_ID"
        value = var.tenant_id
      }
      env {
        name  = "CLIENT_ID"
        value = var.client_id
      }
      env {
        name        = "CLIENT_SECRET"
        secret_name = "client-secret"
      }
      env {
        name  = "ACCOUNT_URL"
        value = var.account_url
      }
    }
  }

}