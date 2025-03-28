terraform {
  required_providers {
    sentry = {
      source  = "jianyuan/sentry"
      version = "0.14.3"
    }
  }

  required_version = ">= 1.11.0"
}

# Looks for a Sentry auth token in the SENTRY_AUTH_TOKEN env var
provider "sentry" {}

module "org" {
  source = "../../modules/organization"
}

module "environments" {
  source = "../../modules/environments"
}

locals {
  environments = {
    idfdev = module.environments.environments.idfdev
  }
}

resource "sentry_project" "project" {
  organization = module.org.org.slug

  teams = [module.org.teams.square.slug]
  name  = "Noteburst"
  slug  = "noteburst"

  platform = "python"
}

module "new_unresolved_alert" {
  for_each     = local.environments
  source       = "../../alerts/new_unresolved/"
  project      = sentry_project.project
  environment  = each.value
  organization = module.org.org
}

