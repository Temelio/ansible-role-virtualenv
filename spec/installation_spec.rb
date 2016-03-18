require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'virtualenv Ansible role' do

    # Declare variables
    packages = Array[]

    if ['debian', 'ubuntu'].include?(os[:family])
        packages = Array[ 'python-dev', 'python-virtualenv' ]
    end

    it 'install role packages' do
        packages.each do |pkg_name|
            expect(package(pkg_name)).to be_installed
        end
    end
end

