#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostProcessConan(base.BoostBaseConan):
    name = "boost_process"
    url = "https://github.com/bincrafters/conan-boost_process"
    lib_short_names = ["process"]
    header_only_libs = ["process"]
    b2_requires = [
        "boost_algorithm",
        "boost_asio",
        "boost_config",
        "boost_core",
        "boost_filesystem",
        "boost_fusion",
        "boost_iterator",
        "boost_move",
        "boost_optional",
        "boost_system",
        "boost_tokenizer",
        "boost_type_index",
        "boost_winapi"
    ]

