{ pkgs, ... }:

{
  packages = [ pkgs.git pkgs.just pkgs.ruff ];

  languages.python = {
    enable = true;
    version = "3.13";
    venv = {
      enable = true;
      requirements = "-e .[dev]";
    };
  };
}
