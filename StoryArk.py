"""
This will be treated as pseudocode for whatever javascript/SQL/PHP/Whatever I end up using in the final product
"""

# Classes
class node:
    def __init__(self, Name, ArcText, *Branches):
        self.name = Name
        self.arcText = ArcText
        self.branches = list(Branches)

    def __str__(self):
        s = "Name: " + self.name + "\nText: " + self.arcText + "\nBranches:"
        for i in self.branches:
            s += " '" + i + "'"
        return s



# Main
def main():
    # Create some nodes
    masterNode = node("Master text Name", "This is the master text", "These", "Are", "Branches")
    theseNode = node("These", "This is the text for the theseNode node", "theseNode1", "theseNode2")
    areNode = node("Are", "areNode Text for looking at", "areNode1", "areNode2")
    branchesNode = node("Branches", "Text for the \"Brances\" node", "branchesNode1", "branchesNode2", "branchesNode3")
    these1Node = node("theseNode1", "This is a second level node")
    these2Node = node("theseNode2", "Also a second level node")
    # Test print a node
    print(branchesNode)
    print(these1Node)
    # Create the master branch
    d = {'master' : masterNode,
        theseNode.name : theseNode,
        areNode.name : areNode,
        branchesNode.name : branchesNode,
        these1Node.name : these1Node,
        these2Node.name : these2Node}
    print(d['master'])
    print(d[d['master'].branches[1]])
    # See what such a branch looks like
    # Edit some nodes
    # Make sure the edits are referenced thus


if __name__ == '__main__':
    main()