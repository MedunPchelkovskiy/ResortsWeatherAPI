provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "fastapi-rg"
  location = "West Europe"
}

resource "azurerm_container_registry" "acr" {
  name                = "fastapireg12345"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_service_plan" "plan" {
  name                = "fastapi-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "app" {
  name                = "fastapi-app-12345"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.plan.id

  site_config {
    application_stack {
      docker_image_name   = "placeholder"
      docker_registry_url = azurerm_container_registry.acr.login_server
    }
  }
}