output "container_app_url" {
  value       = "https://${azurerm_container_app.app.latest_revision_fqdn}"
  description = "Public URL of the Container App"
}

output "container_app_fqdn" {
  value       = azurerm_container_app.app.latest_revision_fqdn
  description = "FQDN of the Container App"
}

output "acr_login_server" {
  value       = azurerm_container_registry.acr.login_server
  description = "ACR login server for docker push"
}
