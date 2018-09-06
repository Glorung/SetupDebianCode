#!/bin/sh

# Create the config directory if it doesn't exist
mkdir -p ./config
mkdir -p ./old_config

# Backing up
rm -rf ./old_config/*
mv ./config/* ./old_config

rm -rf ./config/*
cp -rf ~/.config/terminator/* ./config/
