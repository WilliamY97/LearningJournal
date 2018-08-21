# Common Processes

Snippets of command that are commonly used

## Check if a library or software is already installed and install when it is not

```
 name: Check if X is already installed
  shell: "X --version | awk '{printf $3}'"
  register: X_version_result
  ignore_errors: True

- name: Install X
  yum:
    name: "/usr/local/asgard/packages/hostagent_dcgm/X.rpm"
    state: present
  when: dcgmi_version_result|failed
```

