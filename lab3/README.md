Writing Snort rules to identify attack and apply tested rules. 


Rudimentary Anti-virus program


Read the latest virus definition file to find that a new virus has a particular signature (that
is, the virus contains a specific sequence of bytes). Furthermore, assume that the virus
may use a Caesar-cipher-type of encryption to make itself polymorphic.

Check every file in a specific folder and in all of its subdirectories to find any that are
infected.

For any infected file found, render the virus inactive (set the first 8 bytes of the signature
sequence to “xxxxxxxx”) and quarantine the file (move it to a specified folder).

Keep the user informed (through the UI) about what the program is doing, what infected
files it has found, whether inoculation was done, and whether the dangerous file was
quarantined.
