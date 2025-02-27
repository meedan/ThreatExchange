# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

variable "region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "prefix" {
  description = "Prefix to use for resource names"
  type        = string
}

variable "name" {
  description = "Name of generated dashboard"
  type        = string
}

variable "datastore" {
  description = "DynamoDB Table to store hash and match information into"
  type = object({
    name = string
    arn  = string
  })
}

variable "pipeline_lambdas" {
  description = "Main set of lambdas used in processing content"
  type        = list(tuple([string, string]))
  default     = null
}

variable "api_lambda_name" {
  description = "Name of lambda used as the root api"
  type        = string
  default     = null
}

variable "other_lambdas" {
  description = "Extra lambdas to be included in set of concurrent counts"
  type        = list(string)
  default     = null
}

variable "queues_to_monitor" {
  description = "Main set of sqs queues used in processing content"
  type        = list(tuple([string, string]))
  default     = null
}

variable "api_gateway_id" {
  description = "Id of gateway used to send requests to the api_lambda"
  type        = string
  default     = null
}


