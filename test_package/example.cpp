#include <iostream>
#include <tclap/CmdLine.h>

int main(int argc, const char** argv) {
    TCLAP::CmdLine cmd("test package");

    try {
        cmd.parse(argc, argv);
    } catch (TCLAP::ArgException &e) {
    }

    return 0;
}
