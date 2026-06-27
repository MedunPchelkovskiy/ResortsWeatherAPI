variable "location" {
  type    = string
  default = "West Europe"
}

variable "resource_group_name" {
  type    = string
  default = "portfolio-rg"
}

variable "acr_name" {
  type        = string
  description = "Must be globally unique, alphanumeric only, 5-50 chars."
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
