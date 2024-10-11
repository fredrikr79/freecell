{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
    buildInputs = with pkgs; [
        git
        python312
        python312Packages.pygame    # game rendering
        python312Packages.pytest    # testing
        python312Packages.coverage  # test-coverage
        python312Packages.black     # auto-formatting
        python312Packages.flake8    # style and code quality
    ];
}
