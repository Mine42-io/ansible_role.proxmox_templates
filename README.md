# Ansible role - `proxmox_templates`

Manages KVM templates on Proxmox VE:

* Download images if not already available
* Create and configure KVM templates
  * Support for Cloud-Init templates
* Do not override existing virtual machines

## Tags

| Tags       | Description                            |
|------------|----------------------------------------|
| `setup`    | Create virtual machines templates      |

## Variables

See `defaults/main.yml` for the full list of variables.

| Variable                     | Type            | Required | Default                  | Description                     |
|------------------------------|-----------------|----------|--------------------------|---------------------------------|
| `proxmox_templates_defaults` | `map`           | No       | See `defaults/main.yml`  | Default KVM templates variables |
| `proxmox_templates`          | `list` of `map` | No       | `[]` (empty list)        | KVM templates to create         |

### Configure your templates

This role creates the templates defined in `proxmox_templates`:

```yaml
proxmox_templates:
  - id: 9000
    name: "ubuntu-20.04-cloudinit"
    image: "focal-server-cloudimg-amd64.img"
    image_url: "https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img"
  # ...
```

`proxmox_templates` items requires only the `id`, `name` and `image` attributes.
All other attributes are merged from `proxmox_templates_defaults`.

You may override `proxmox_templates_defaults` with your own defaults (e.g. using an external `vars` file).

Supported variables:

| Variable        | Type               | Required | Default                                      | Description                                              |
|-----------------|--------------------|----------|----------------------------------------------|----------------------------------------------------------|
| `id`            | `integer`          | Yes      |                                              | KVM template ID (must be unique)                         |
| `name`          | `string`           | Yes      |                                              | KVM template name (must be unique)                       |
| `image`         | `string`           | Yes      |                                              | KVM image (OS) name                                      |
| `cores`         | `integer`          | No       | `1`                                          | Number of CPU cores                                      |
| `sockets`       | `integer`          | No       | `1`                                          | Number of CPU sockets                                    |
| `memory`        | `integer`          | No       | `512`                                        | Memory size (in Mb)                                      |
| `networks`      | `list` of `string` | No       | `["model=virtio,bridge=vmbr1,firewall=1", ]` | List of VM networks                                      |
| `image_url`     | `string`           | No       |                                              | Image URL to download automatically                      |
| `image_dirname` | `string`           | No       | `/var/lib/vz/template/iso"`                  | Store downloaded image in this directory                 |
| `image_storage` | `string`           | No       | `local`                                      | Image storage type (`local`, `local-lvm`, ...)           |
| `cinit`         | `bool`             | No       | `true`                                       | True if this is a Cloud-Init template                    |
| `cinit_storage` | `string`           | No       | `local`                                      | Cloud-Init disk storage type (`local`, `local-lvm`, ...) |

## Filter plugins

| Filter      | File      | Description                                          |
|-------------|-----------|------------------------------------------------------|
| `map_list`  | `main.py` | Tramsforms a `list` of `string` to a `list` of `map` |
| `aggregate` | `main.py` | Transforms a `list` of `map` to a `map` of `map`     |

## External resources

* https://pve.proxmox.com/pve-docs/qm.1.html
* https://docs.openstack.org/image-guide/obtain-images.html
