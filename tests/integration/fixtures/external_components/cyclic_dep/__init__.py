# Minimal component "cyclic_dep" that depends on itself
import esphome.config_validation as cv

DEPENDENCIES = ["cyclic_dep"]

CONFIG_SCHEMA = cv.Schema({})
