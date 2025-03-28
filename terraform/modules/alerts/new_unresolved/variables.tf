variable "environment" {
  description = "Info about the environment for triggering the alert"
  type = object({
    name = string
    status_channel = object(
      {
        name = string
    })
  })
}

variable "organization" {
  description = "The organization in which to provision this alert"
  type        = object({ slug = string })
}

variable "project" {
  description = "Trigger the alert for this project"
  type = object({
    slug = string
  })
}

variable "renotify_interval" {
  description = "If and how often to re-notify for existing unresolved issues. If not provided, then only one notification will be sent when a new issue is created or a resolved issue becomes unresolved again. If provided, Valid values are: 5m, 15m, 1h, 1d, 1w, and 30d"
  type        = string
  default     = null
}
