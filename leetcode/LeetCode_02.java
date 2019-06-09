/**
 * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
 * 
 * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
 * 
 * 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 
 * 示例：
 * 
 * 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4) 输出：7 -> 0 -> 8 原因：342 + 465 = 807
 * 
 * 来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/add-two-numbers
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 * 
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */
class Solution {
    /**
     * 思路还是通过每位相加，记录是否需要进位然后在下一次相加时考虑上进位的值，整体不难，完全不了解ListNode用法导致话费时间较长
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // ListNode只有带参构造
        ListNode result = new ListNode(0);

        ListNode current = result;
        // 记录进位
        int carry = 0;

        while (l1 != null || l2 != null) {
            // 考虑链表长度不一致的情况
            int x = l1 == null ? 0 : l1.val;
            int y = l2 == null ? 0 : l2.val;
            int sum = x + y + carry;

            carry = sum / 10;
            // 如果是给ListNode当前val处理起来会很麻烦
            current.next = new ListNode(sum % 10);

            current = current.next;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }

        // 考虑最后一次是否有进位
        if (carry > 0) {
            current.next = new ListNode(carry);
        }

        // 为了丢弃掉初始化时首位的0
        return result.next;
    }
}