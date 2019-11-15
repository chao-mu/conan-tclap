from conans import ConanFile, CMake, tools

class TclapConan(conans.ConanFile):
    name = "tclap"
    version = "1.2.2"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def file_path(self):
        return "tclap-%s" % self.version

    def source(self):
        zip_file = "tclap-%s.tar.gz" % self.version
        url = "https://iweb.dl.sourceforge.net/project/tclap/" + zip_file
        tools.download(url)
        tools.unzip(zip_file)

    def package(self):
        self.copy("*.h", dst="include/tclap", src=("%s/include/tclap" % self.file_path))
