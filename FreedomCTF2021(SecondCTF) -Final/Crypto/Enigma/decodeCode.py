from enigma.machine import EnigmaMachine

for a in range(1, 26):
    for b in range(1, 26):
        for c in range(1, 26):
            machine = EnigmaMachine.from_key_sheet(
                rotors='I II III',
                reflector='B',
                ring_settings=[a, b, c],
                plugboard_settings='GD HR IC KO ML QU PZ WA FN BS')
            machine.set_display('IQL')
            ciphertext = 'cazmgsczlrkrkmnlhsvvma'
            plaintext = machine.process_text(ciphertext)
            print(plaintext)



