# Console Commands Over HTTP (CCOH)

CCOH is a powerful tool designed to provide an alternative to SSH for executing console commands. This tool can be particularly useful in scenarios where SSH may not be viable or preferred.

## Features

- Execute console commands over HTTP
- Easy integration with existing systems
- Designed to work in combination with Shadowsocks for secure communication

## Prerequisites

- **Shadowsocks**: CCOH is meant to be used alongside Shadowsocks for secure data transmission. Please ensure you have Shadowsocks installed and configured on your system. Note that Shadowsocks does not come bundled with CCOH and must be set up separately.

## Installation

To install CCOH, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/NuggetBugget5/CCOH.git
    cd CCOH
    ```

2. **Start the Server**:

    ```bash
    sudo python3 main.py
    ```

3. **Start Using CCOH**:

    - Open your preferred web browser
    - Type `{your local IP address}:443`
    - Press Enter/Return

Important note: The default password is `iamlosingpixels`. This can be manually changed by creating a new SHA-256 hash of a password and overwriting the contents of `hash.key` in the `Hash` folder. A feature to do this automatically may come in the future.

## Security Considerations

Ensure that CCOH is used in a secure environment and that the HTTP endpoint is not exposed to untrusted networks. Use Shadowsocks to encrypt and secure the communication between the client and the CCOH server.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
