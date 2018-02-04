#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostProcessConan(ConanFile):
    name = "boost_process"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost_process"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["process"]
    is_header_only = True

    def package_id_additional(self):
        self.info.header_only()

    requires = (
        "boost_package_tools/1.65.1@bincrafters/testing",
        "boost_algorithm/1.65.1@bincrafters/testing",
        "boost_asio/1.65.1@bincrafters/testing",
        "boost_config/1.65.1@bincrafters/testing",
        "boost_core/1.65.1@bincrafters/testing",
        "boost_filesystem/1.65.1@bincrafters/testing",
        "boost_fusion/1.65.1@bincrafters/testing",
        "boost_iterator/1.65.1@bincrafters/testing",
        "boost_move/1.65.1@bincrafters/testing",
        "boost_optional/1.65.1@bincrafters/testing",
        "boost_system/1.65.1@bincrafters/testing",
        "boost_tokenizer/1.65.1@bincrafters/testing",
        "boost_type_index/1.65.1@bincrafters/testing",
        "boost_winapi/1.65.1@bincrafters/testing"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.65.1@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
