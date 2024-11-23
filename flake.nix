{
  description = "Todo";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem ( system:
    let
      pkgs = import nixpkgs { inherit system; };
      texliveEnv = with pkgs; texlive.combine {
        inherit (texlive)
          scheme-medium
          pdftex
          collection-langenglish
          collection-langcyrillic

          comment
          epigraph
          expdlist
          nextpage
        ;
      };

    in {
      devShells = rec {
        default = pkgs.mkShell {
          name = "latex-minimal";
          buildInputs = with pkgs; [
            texliveEnv
          ];
        };
      };
    });
}
