udp6       0      0 localhost:323           [::]:*                              root       22225      1003/chronyd        
udp6       0      0 [::]:51802              [::]:*                              rpcuser    64331637   1179313/rpc.statd   
udp6       0      0 [::]:hydap              [::]:*                              root       95716880   1622333/klnagent    

=== Output from cmp-db-test ===
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       User       Inode      PID/Program name    
tcp        0      0 0.0.0.0:sunrpc          0.0.0.0:*               LISTEN      root       8142000    1/systemd           
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      root       22624      945/sshd: /usr/sbin 
tcp        0      0 0.0.0.0:XmlIpcRegSvc    0.0.0.0:*               LISTEN      root       8211276    85736/docker-proxy  
tcp        0      0 0.0.0.0:27017           0.0.0.0:*               LISTEN      root       8190137    77836/docker-proxy  
tcp        0      0 localhost:34291         0.0.0.0:*               LISTEN      root       35460275   3206229/klnagent    
tcp        0      0 0.0.0.0:19093           0.0.0.0:*               LISTEN      root       8213974    85751/docker-proxy  
tcp        0      0 localhost:30523         0.0.0.0:*               LISTEN      root       35460286   3206229/klnagent    
tcp        0      0 cmp-db-test:ssh         10.28.4.190:37668       ESTABLISHED root       64490677   2394655/sshd: root  
tcp6       0      0 localhost:30523         [::]:*                  LISTEN      root       35460285   3206229/klnagent    
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      root       8140914    1/systemd           
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      root       22633      945/sshd: /usr/sbin 
tcp6       0      0 localhost:34291         [::]:*                  LISTEN      root       35460276   3206229/klnagent    
tcp6       0      0 [::]:websm              [::]:*                  LISTEN      root       20348      1/systemd           
tcp6       0      0 [::]:XmlIpcRegSvc       [::]:*                  LISTEN      root       8212362    85742/docker-proxy  
tcp6       0      0 [::]:27017              [::]:*                  LISTEN      root       8190140    77844/docker-proxy  
tcp6       0      0 localhost:9879          [::]:*                  LISTEN      root       35463123   3207042/kesl        
tcp6       0      0 localhost:9789          [::]:*                  LISTEN      root       35463124   3207042/kesl        
tcp6       0      0 [::]:19093              [::]:*                  LISTEN      root       8213977    85758/docker-proxy  
udp        0      0 0.0.0.0:hydap           0.0.0.0:*                           root       35461155   3206229/klnagent    
udp        0      0 0.0.0.0:sunrpc          0.0.0.0:*                           root       8142007    1/systemd           
udp        0      0 localhost:323           0.0.0.0:*                           root       23667      1294/chronyd        
udp6       0      0 [::]:hydap              [::]:*                              root       35461156   3206229/klnagent    
udp6       0      0 [::]:sunrpc             [::]:*                              root       8142873    1/systemd           
udp6       0      0 localhost:323           [::]:*                              root       23668      1294/chronyd        

=== Output from iw-tms ===
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       User       Inode      PID/Program name    
tcp        0      0 0.0.0.0:8540            0.0.0.0:*               LISTEN      iwtm       38233      2517/iw_pas         
tcp        0      0 0.0.0.0:ismserver       0.0.0.0:*               LISTEN      iwtm       12112      2524/iw_indexer     
tcp        0      0 0.0.0.0:9310            0.0.0.0:*               LISTEN      iwtm       41211      3655/searchd        
tcp        0      0 0.0.0.0:sphinxapi       0.0.0.0:*               LISTEN      iwtm       45077      3982/searchd     
