#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
from setuptools import setup, find_packages, Extension
import glob
import itertools
import os
import sys
import subprocess
import numpy

if not os.path.exists('/usr/lib/liblibmarisa-trie.so'):
    subprocess.call("sudo bash ./install_dep.sh", shell=True)
subprocess.call("sudo bash ./update_cpp.sh", shell=True)

MARISA_ROOT_DIR = "marisa-trie"
MARISA_SOURCE_DIR = os.path.join(MARISA_ROOT_DIR, "lib")
MARISA_INCLUDE_DIR = os.path.join(MARISA_ROOT_DIR, "include")
MARISA_FILES = [
    "marisa/*.cc",
    "marisa/grimoire.cc",
    "marisa/grimoire/io/*.cc",
    "marisa/grimoire/trie/*.cc",
    "marisa/grimoire/vector/*.cc",
]

MARISA_FILES[:] = itertools.chain(
    *(glob.glob(os.path.join(MARISA_SOURCE_DIR, path))
    for path in MARISA_FILES))


ext_modules = [
    Extension(
        "lingutok.core", [
            "lingutok/agent.cpp",
            "lingutok/base.cpp",
            "lingutok/iostream.cpp",
            "lingutok/key.cpp",
            "lingutok/keyset.cpp",
            "lingutok/core.cpp",
            "lingutok/query.cpp",
            "lingutok/std_iostream.cpp",
            "lingutok/trie.cpp"
        ], 
        include_dirs=[MARISA_INCLUDE_DIR, "utf8proc","OpenCC/src",numpy.get_include()],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    ),
]

setup(
    name='lingutok',
    packages = find_packages(),
    version='0.0.1',
    description='Linguistic Tokenizer',
    libraries=[("libmarisa-trie", {
        "sources": MARISA_FILES,
        "include_dirs": [MARISA_SOURCE_DIR, MARISA_INCLUDE_DIR]
    }), ("libutf8proc", {
        "sources": ["utf8proc/utf8proc.c"],
        "include_dirs": ["utf8proc"]
    }), ("libopencc", {
        "sources": [
            "OpenCC/src/Config.cpp",
            "OpenCC/src/Conversion.cpp",
            "OpenCC/src/ConversionChain.cpp",
            "OpenCC/src/Converter.cpp",
            "OpenCC/src/Dict.cpp",
            "OpenCC/src/DictConverter.cpp",
            "OpenCC/src/DictEntry.cpp",
            "OpenCC/src/DictGroup.cpp",
            "OpenCC/src/Lexicon.cpp",
            "OpenCC/src/MarisaDict.cpp",
            "OpenCC/src/MaxMatchSegmentation.cpp",
            "OpenCC/src/PhraseExtract.cpp",
            "OpenCC/src/SerializedValues.cpp",
            "OpenCC/src/SimpleConverter.cpp",
            "OpenCC/src/Segmentation.cpp",
            "OpenCC/src/TextDict.cpp",
            "OpenCC/src/UTF8StringSlice.cpp",
            "OpenCC/src/UTF8Util.cpp"
        ],
        "include_dirs": [
            "OpenCC/deps/gtest-1.7.0/include",
            "OpenCC/deps/tclap-1.2.2",
            "OpenCC/deps/rapidjson-1.1.0",
            "OpenCC/deps/marisa-0.2.5/include",
            "OpenCC/deps/libdarts/src",
            "OpenCC/deps/darts-clone",
            "OpenCC/src"
        ],
        "extra_compile_args":[
            "-DBUILD_DOCUMENTATION:BOOL=ON",
            "-DENABLE_GTEST:BOOL=OFF",
            "-DENABLE_BENCHMARK:BOOL=OFF",
            "-DCMAKE_BUILD_TYPE=Release",
        ]
    })],
    ext_modules=ext_modules,
    setup_requires=['Cython','numpy'],
    package_data={'lingutok': ['resources/*', 'resources/opencc_config/*']}
)

