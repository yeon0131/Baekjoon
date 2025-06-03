// 11650번 자바 버전 풀이

import java.util.*;

public class boj_11650 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] points = new int[n][2]; // 2차원 배열로 좌표 저장

        for (int i = 0; i < n; i++){
            points[i][0] = sc.nextInt(); // x좌표
            points[i][1] = sc.nextInt(); // y좌표
        }

        // 정렬: x 오름차순, x가 같으면 y 오름차순
        Arrays.sort(points, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if (a[0] == b[0]) {
                    return a[1] - b[1]; // y 기준 정렬 
                }
                return a[0] - b[0]; // x 기준 정렬
            }
        });

        //출력
        for (int[] point : points) {
            System.out.println(point[0] + " " + point[1]);
        }

        sc.close();
    }
}