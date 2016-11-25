import configparser
import os

# Name of the script and the service file
script_name = 'pythonservice'
description = 'My Python Service'

working_dir = os.path.dirname(os.path.realpath(__file__))

# Don't modify following paths!
script_file = '{}.sh'.format(script_name)
service_file = '/lib/systemd/system/{}.service'.format(script_name)

def main():
    config = configparser.ConfigParser()
    config.optionxform = str

    config.add_section('Unit')
    config.add_section('Service')
    config.add_section('Install')

    config['Unit']['Description'] = description
    config['Unit']['After'] = 'multi-user.target'
    config['Service']['Type'] = 'simple'
    config['Service']['WorkingDirectory'] = working_dir
    config['Service']['ExecStart'] = os.path.join(working_dir, script_file)
    config['Install']['WantedBy'] = 'multi-user.target'

    with open(service_file, 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    main()
