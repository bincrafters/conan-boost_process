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
        "boost_package_tools/1.65.1@bincrafters/stable",
        "boost_algorithm/1.65.1@bincrafters/stable",
        "boost_asio/1.65.1@bincrafters/stable",
        "boost_config/1.65.1@bincrafters/stable",
        "boost_core/1.65.1@bincrafters/stable",
        "boost_filesystem/1.65.1@bincrafters/stable",
        "boost_fusion/1.65.1@bincrafters/stable",
        "boost_iterator/1.65.1@bincrafters/stable",
        "boost_move/1.65.1@bincrafters/stable",
        "boost_optional/1.65.1@bincrafters/stable",
        "boost_system/1.65.1@bincrafters/stable",
        "boost_tokenizer/1.65.1@bincrafters/stable",
        "boost_type_index/1.65.1@bincrafters/stable",
        "boost_winapi/1.65.1@bincrafters/stable"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.65.1@bincrafters/stable"

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
