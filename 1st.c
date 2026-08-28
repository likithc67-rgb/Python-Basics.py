#include<stdio.h>

int a, b, u, v, n, i, j, ne = 1;
int visited[10] = {0}, min, mincost = 0, cost[10][10];

void main()
{
    printf("\nEnter the number of nodes: ");
    scanf("%d", &n);

    printf("\nEnter the adjacency matrix:\n");

    // Reading adjacency matrix
    for(i = 1; i <= n; i++)
    {
        for(j = 1; j <= n; j++)
        {
            scanf("%d", &cost[i][j]);

            // Replace 0 with 999
            if(cost[i][j] == 0)
                cost[i][j] = 999;
        }
    }

    // Start from node 1
    visited[1] = 1;

    printf("\nThe edges of Minimum Cost Spanning Tree are:\n");

    while(ne < n)
    {
        // Find minimum edge
        for(i = 1, min = 999; i <= n; i++)
        {
            for(j = 1; j <= n; j++)
            {
                if(cost[i][j] < min)
                {
                    if(visited[i] != 0)
                    {
                        min = cost[i][j];
                        a = u = i;
                        b = v = j;
                    }
                }
            }
        }

        // Check cycle condition
        if(visited[u] == 0 || visited[v] == 0)
        {
            printf("\nEdge %d : (%d -> %d) Cost = %d",
                   ne++, a, b, min);

            mincost = mincost + min;

            visited[b] = 1;
        }

        // Remove selected edge
        cost[a][b] = cost[b][a] = 999;
    }

    printf("\n\nMinimum Cost = %d\n", mincost);
}