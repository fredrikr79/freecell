{
  description = "A game of solitaire written in Python with Pygame";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let 
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    pypkgs = pkgs.python3Packages;
    dependencies = with pypkgs; [
        pygame-ce    # game rendering
    ];
    build-system = with pypkgs; [
        setuptools   # packaging
    ];
    nativeCheckInputs = with pypkgs; [
        # pytestCheckHook
    ];
    pytestFlagsArray = [

    ];
    inherit (pkgs) lib;
  in {

    # packages.x86_64-linux.hello = nixpkgs.legacyPackages.x86_64-linux.hello;
    #
    # packages.x86_64-linux.default = self.packages.x86_64-linux.hello;

    packages.${system}.default = pypkgs.buildPythonApplication {
        name = "freecell";

        inherit nativeCheckInputs build-system dependencies; 

        src = lib.sources.cleanSource ./.;
    };

    # apps.${system}.default = {
    #     type = "app";
    #     program = packages.${system}.default = 
    # };

    devShells.${system}.default = pkgs.mkShell {
        packages = with pypkgs; [
            black        # auto-formatting
            flake8       # style and code quality
            coverage     # test-coverage
        ] ++ dependencies ++ build-system ++ nativeCheckInputs;
    };

  };
}
