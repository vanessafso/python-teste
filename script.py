#!/usr/bin/env python3

from os import environ

print("Hello World!!")

## Testando Variáveis
test_variable = "env.TEST_VARIABLE"

print(test_variable)

print(test_variable['env.TEST_VARIABLE'])

#env_dict = dict(environ)
#print(env_dict["USER"], env_dict["NAME"])