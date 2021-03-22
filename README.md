# CausalityChecker: Usage

## Installation

Just type:

```gmake distclean && gmake all```

## Running

Just type:

```./check_causality /path/to/file/to/check```

The output files will be stored in the same directory that the file to check is located.  Note that all quantities in the file must be in units of fm!

## Generating Animations

You can run the causality check analysis and generate animations of the results automatically by typing:

```bash run_job.sh /path/to/file/to/check```

The output files (or the sub-directories containing them) will be stored in the same directory that the file to check is located.

