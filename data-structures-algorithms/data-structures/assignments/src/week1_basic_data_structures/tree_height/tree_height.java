import java.util.*;
import java.io.*;

public class tree_height {
    class FastScanner {
        StringTokenizer tok = new StringTokenizer("");
        BufferedReader in;

        FastScanner() {
            in = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() throws IOException {
            while (!tok.hasMoreElements())
                tok = new StringTokenizer(in.readLine());
            return tok.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    public class TreeNode {
        int data;
        List<TreeNode> children = new ArrayList<>();

        public TreeNode(int data) {
            this.data = data;
        }
    }

    public class TreeHeight {
        int n;
        int parent[];
        TreeNode root;

        void read() throws IOException {
            FastScanner in = new FastScanner();
            n = in.nextInt();
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = in.nextInt();
            }
        }

        TreeNode[] getTree() {
            TreeNode[] nodes = new TreeNode[n];

            for (int i = 0; i < n; i++) {
                nodes[i] = new TreeNode(0);
            }

            for (int i = 0; i < n; i++) {
                if (parent[i] == -1) {
                    root = new TreeNode(i);
                } else {
                    nodes[parent[i]].data = i;
                    nodes[parent[i]].children.add(nodes[i]);
                }
            }

            return nodes;
        }

        int computeHeight() {
            // Replace this code with a faster implementation
            TreeNode[] nodes = getTree();

            return computeHeightUtil(nodes[root.data]);

        }

        int computeHeightUtil(TreeNode node) {

            if (node == null) {
                return 0;
            } else if (node.children.size() == 0) {
                return 1;
            } else {
                List<TreeNode> children = node.children;

                int maxHeight = 0;

                for (int i = 0; i < children.size(); i++) {
                    maxHeight = Math.max(maxHeight, computeHeightUtil(children.get(i)));
                }

                return 1 + maxHeight;
            }

        }


    }

    static public void main(String[] args) throws IOException {
        new Thread(null, new Runnable() {
            public void run() {
                try {
                    new tree_height().run();
                } catch (IOException e) {
                }
            }
        }, "1", 1 << 26).start();
    }

    public void run() throws IOException {
        TreeHeight tree = new TreeHeight();
        tree.read();
        System.out.println(tree.computeHeight());
    }
}
