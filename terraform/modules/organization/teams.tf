data "sentry_team" "square" {
  organization = data.sentry_organization.org.slug
  slug         = "square"
}

