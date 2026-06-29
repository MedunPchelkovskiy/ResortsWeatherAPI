variable "location" {
  type    = string
  default = "Poland"
}

variable "resource_group_name" {
  type    = string
  default = "portfolio-rg"
}

variable "acr_name" {
  type        = string
  description = "Must be globally unique, alphanumeric only, 5-50 chars."
  validation {
    condition     = can(regex("^[a-zA-Z0-9]{5,50}$", var.acr_name))
    error_message = "ACR името трябва да съдържа 5-50 буквено-цифрени знака."
  }
}

variable "environment_name" {
  type    = string
  default = "portfolio-env"
}

variable "container_app_name" {
  type    = string
  default = "resort-weather-api"
}

variable "docker_image" {
  type        = string
  description = "Image name in ACR, e.g. fastapi-api"
}

variable "docker_tag" {
  type    = string
  default = "latest"
}

variable "tenant_id" {
  type      = string
  sensitive = true
}

variable "client_id" {
  type      = string
  sensitive = true
}

variable "client_secret" {
  type      = string
  sensitive = true
}

variable "account_url" {
  type    = string
  default = "https://etlflowrawdata.dfs.core.windows.net"
}