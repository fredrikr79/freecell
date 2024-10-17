{
  description = "A game of solitaire written in Python with Pygame using Nix";

  inputs = {
    # nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    pyproject-nix = {
      url = "github:nix-community/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, pyproject-nix, ... }: let 
    inherit (nixpkgs) lib;
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    pyproject = pyproject-nix.lib.project.loadPyproject {
      projectRoot = ./.;
    };
    python = pkgs.python3;
  in {

    # packages.x86_64-linux.hello = nixpkgs.legacyPackages.x86_64-linux.hello;
    #
    # packages.x86_64-linux.default = self.packages.x86_64-linux.hello;

    packages.${system}.default = let
      attrs = pyproject.renderers.buildPythonPackage { inherit python; };
    in python.pkgs.buildPythonApplication (attrs // {
      extrasAttrMappings = {
        testing = "checkInputs";
      };
    });

    apps.${system}.default = {
        type = "app";
        program = "self.packages.${system}.default/bin/freecell";
    };

    devShells.${system}.default = let 
      arg = pyproject.renderers.withPackages { 
        inherit python; 
        extras = builtins.attrNames pyproject.optional-dependencies.formatting;
      };
      pythonEnv = python.withPackages (arg);
    in pkgs.mkShell {
        packages = [ pythonEnv. ];
    };

  };
}
