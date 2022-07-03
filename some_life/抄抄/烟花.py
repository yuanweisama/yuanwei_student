# 初始化烟花参数void Init(int i )
{    # 分别为：烟花中心到图片边缘的最远距离、烟花中心到图片左上角的距离(x、y) 两个分量
    int r[13] = {120, 120, 155, 123, 130, 147, 138, 138, 130, 135, 140, 132, 155},
    int x[13] = {120, 120, 110, 117, 110, 93, 102, 102, 110, 105, 100, 108, 110},
    int y[13] = {120, 120, 85, 118, 120, 103, 105, 110, 110, 120, 120, 104, 85},
    ''' 初始化烟花 '''

    Fire[i].x = 0; # 烟花中心坐标
    Fire[i].y = 0;
    Fire[i].width = 240; # 图片宽
    Fire[i].height = 240; # 图片高
    Fire[i].max_r = r[i]; # 最大半径
    Fire[i].cen_x = x[i]; # 中心距左上角距离
    Fire[i].cen_y = y[i];
    Fire[i].show = false; # 是否绽放
    Fire[i].dt = 5; # 绽放时间间隔
    Fire[i].t1 = timeGetTime();
    Fire[i].r = 0; # 从0开始绽放

    /**** 初始化烟花弹 *****/

    Jet[i].x = -240; # 烟花弹左上角坐标
    Jet[i].y = -240;
    Jet[i].hx = -240; # 烟花弹发射最高点坐标
    Jet[i].hy = -240;
    Jet[i].height = 0; # 发射高度
    Jet[i].t1 = timeGetTime();
    Jet[i].dt = rand() % 10; # 发射速度时间间隔
    Jet[i].n = 0; # 烟花弹闪烁图片下标
    Jet[i].shoot = false; # 是否发射}

# 加载图片void Load()
{''' 储存烟花的像素点颜色 '''
    IMAGE fm, gm,
    loadimage( & fm, "./fire/flower.jpg", 3120, 240 );
    for (int i = 0; i < 13; i++)
    {
        SetWorkingImage( & fm );
        getimage( & gm, i * 240, 0, 240, 240 );
        SetWorkingImage( & gm );
        for ( int a = 0; a < 240; a++ ) for ( int b = 0; b < 240; b++ )
            Fire[i].xy[a][b] = getpixel( a, b );
    }

    IMAGE sm;
    loadimage( & sm, "./fire/shoot.jpg", 200, 50 );
    for ( i = 0; i < 13; i++ )
    {
        SetWorkingImage( & sm );        int n = rand() % 5;

        getimage( & Jet[i].img[0], n * 20, 0, 20, 50 );
        getimage( & Jet[i].img[1], (n + 5) * 20, 0, 20, 50 );
    }

    IMAGE hm;
    loadimage( & hm, "./fire/happy.jpg", 689, 115 );
    SetWorkingImage( & hm );
    for ( i = 0; i < 13; i++ )
    {
        Happy[i].x = i * 90;
        Happy[i].y = rand() % 100 + 500;
        getimage( & Happy[i].img, i * 53, 0, 53, 115 );
    }

    Wish.x        = 0;
    Wish.y        = 100;
    Wish.t1        = timeGetTime();
    Wish.dt        = 46;
    Wish.dir    = 0;
    Wish.dxy    = rand() % 8 + 1;
    loadimage( & Wish.img, "./fire/yaojing.jpg", 490, 100 );
    putimage( Wish.x, Wish.y, & Wish.img, SRCINVERT );

    SetWorkingImage();
}

# 扫描烟花弹并发射void Shoot()
{   for (int i = 0; i < 13; i++)
   {
    Jet[i].t2 = timeGetTime();
    if ( Jet[i].t2 - Jet[i].t1 > Jet[i].dt & & Jet[i].shoot == true )
    {/ ** ** 烟花弹的上升 ** ** * /
        putimage( Jet[i].x, Jet[i].y, & Jet[i].img[Jet[i].n], SRCINVERT );
        if ( Jet[i].y > Jet[i].hy )
        {
            Jet[i].n++;
            Jet[i].y -= 5;
        }

        putimage( Jet[i].x, Jet[i].y, & Jet[i].img[Jet[i].n], SRCINVERT );
        / ** ** 上升到高度的 3 / 4，减速 ** ** * /
        if ( (Jet[i].y - Jet[i].hy) * 4 < Jet[i].height )
        Jet[i].dt = rand() % 4 + 10;
        / ** ** 上升到最大高度 ** ** * /
        if ( Jet[i].y <= Jet[i].hy )
        {# 播放爆炸声
            char c1[50], c2[30], c3[30];
            sprintf( c1, "open ./fire/bomb.wav alias n%d", i );
            sprintf( c2, "play n%d", i );
            sprintf( c3, "close s%d", i );

            mciSendString( c3, 0, 0, 0 );
            mciSendString( c1, 0, 0, 0 );
            mciSendString( c2, 0, 0, 0 );

            putimage( Jet[i].x, Jet[i].y, & Jet[i].img[Jet[i].n], SRCINVERT ); # 擦掉烟花弹
            Fire[i].x = Jet[i].hx + 10; # 在烟花弹中间爆炸
            Fire[i].y = Jet[i].hy; # 在最高点绽放
            Fire[i].show = true; # 开始绽放
            Jet[i].shoot = false; # 停止发射
            # 显示对应字母
            putimage( Happy[HAPPY::
            num].x, Happy[HAPPY::num].y, & Happy[HAPPY::num].img, SRCINVERT );
            HAPPY::num + +;
            if (HAPPY::num > 12)
                HAPPY::num = 0;
        }
        Jet[i].t1 = Jet[i].t2;
    }
  }
}
