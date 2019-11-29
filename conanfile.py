from conans import ConanFile, CMake, tools

class TclapConan(ConanFile):
    name = "tclap"
    settings = "os", "compiler", "build_type", "arch"
    topics = ("conan", "tclap", "cli")
    _source_subfolder = "tclap"

    def source(self):
        meta = self.conan_data["sources"][self.version]
        zip_path = "tclap.tar.gz"
        tools.download(meta["url"], zip_path)
        tools.unzip(zip_path, self._source_subfolder)

    def package(self):
        self.copy("include/tclap/*.h", dst=".", src=self._source_subfolder)
