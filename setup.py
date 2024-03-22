from setuptools import setup
import os
from glob import glob

package_name = 'practice_mazes'

orig_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml'])
    ]

def dir_files(directory_list):
    new_data_files = orig_files
    install_path = ''
    path_files = []
    first_loop = True
    for directory in directory_list:
        for (dirpath, dirnames, files) in os.walk(directory):
            for f in files:
                file_path = os.path.join(dirpath,f)
                if dirpath == 'rviz':
                    dirpath = 'config'
                new_install_path = os.path.join('share', package_name, dirpath)
                if new_install_path == install_path:
                    path_files.append(file_path)
                else:
                    if not first_loop:
                        new_data_files.append((install_path, path_files))
                    path_files = [file_path]
                    install_path = new_install_path
                    first_loop = False
    new_data_files.append((install_path, path_files))
    return new_data_files

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=dir_files(['launch', 'models', 'worlds']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeffm',
    maintainer_email='jeffm@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)