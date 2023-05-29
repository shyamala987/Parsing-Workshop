#!/bin/bash

print_my_argument() {
  echo $1
}

print_my_argument
print_my_argument Hello
print_my_argument "Hello World"
print_my_argument Hello World
