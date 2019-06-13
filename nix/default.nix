{
  config_exporters = { optionalAttrs, ... }: [
    (config: { vultr = optionalAttrs (config.deployment.targetEnv == "vultr") config.deployment.vultr; })
  ];
  options = [
    ./vultr.nix
  ];
  resources = { evalResources, zipAttrs, resourcesByType, ... }: { };
}
