# Playbooks
  
Ansible playbook is a set of sequential tasks. Instead of running each task one by one manually - we write the commands in a playbook. This is like a shell script or bash script.

Example:

```
---
- hosts: demo_hosts
  vars:
    package1 : "nginx"
    package2 : "wget"
  tasks:
    - name: Installing package nginx
      apt: pkg=nginx state=installed update_cache=true
      become: true
    - name: Installing wget
      apt: name={{ package2 }} state=installed update_cache=true
      become: true
    - name: Copying test1 file
      copy: src=/tmp/test11 dest=/tmp/test11
```
