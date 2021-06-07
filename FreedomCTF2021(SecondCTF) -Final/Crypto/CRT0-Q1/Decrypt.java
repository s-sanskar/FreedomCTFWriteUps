public class Decrypt {
    public static void main(String[] args) {
        String decodePhrase = "l4butzb9`b`oJ`fmef4O";
        decodePhrase = decodePhrase.replace('Z', '~');
        decodePhrase = decodePhrase.replace('Q', '%');

        char[] chars = decodePhrase.toCharArray();

        for (int first = 1; first < 5; first++) {
            String code = "";
            System.out.print("First: ");
            for (char c : chars) {
                c -= first;
                System.out.print(c);
                code += Character.toString(c);
            }
            System.out.println("");
            String rw = "";
            for (int j = code.length() -1; j >= 0; j--) {
                rw = rw + code.charAt(j);
            }
            System.out.print("Second: " + rw + "\n");
            System.out.println("");
        }
    }
}
