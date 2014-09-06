from distutils.command.install import install
from distutils.core import setup
import os.path
import json
import sys

kernel_json = {
    "argv": [sys.executable, 
	     "-m", "processing_kernel", 
	     "-f", "{connection_file}"],
    "display_name": "Processing",
    "language": "java"
}

class install_with_kernelspec(install):
    def run(self):
        install.run(self)
        from IPython.kernel.kernelspec import KernelSpecManager
        from IPython.utils.path import ensure_dir_exists
        destdir = os.path.join(KernelSpecManager().user_kernel_dir, 
                               'processing_kernel')
        ensure_dir_exists(destdir)
        with open(os.path.join(destdir, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)

svem_flag = '--single-version-externally-managed'
if svem_flag in sys.argv:
    # Die, setuptools, die.
    sys.argv.remove(svem_flag)

setup(name='processing_kernel',
      version='0.4',
      description='A Processing kernel for Jupyter/IPython',
      long_description="A Processing kernel for Jupyter/IPython, based on MagicKernel",
      url="https://github.com/blink1073/jupyter_kernel/tree/master/processing_kernel",
      author='Douglas Blank',
      author_email='doug.blank@gmail.com',
      py_modules=['processing_kernel'],
      install_requires=["jupyter_kernel"],
      cmdclass={'install': install_with_kernelspec},
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
          'Topic :: System :: Shells',
      ]
)
