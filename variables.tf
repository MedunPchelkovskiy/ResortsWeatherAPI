variable "resource_group_name" {
  type    = string
  default = "fastapi-rg"
}

variable "location" {
  type    = string
  default = "West Europe"
}

variable "acr_name" {
  type = string
}

variable "app_name" {
  type = string
}

variable "service_plan_name" {
  type    = string
  default = "fastapi-plan"
}