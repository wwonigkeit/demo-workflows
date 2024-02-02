terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

variable "aws_key" {
  type = string
}

variable "aws_secret" {
  type = string
}

provider "aws" {
  region  = "ap-southeast-2"
  access_key = var.aws_key
  secret_key = var.aws_secret
}

resource "aws_instance" "app_server" {
  ami           = "ami-0e812285fd54f7620"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleTerraformMachine"
  }
}