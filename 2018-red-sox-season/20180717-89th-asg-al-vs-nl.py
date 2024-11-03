import os
from baseball_scorecard.baseball_scorecard import Scorecard

# AL All-Stars @ NL All-Stars, 2018-07-17
# https://www.baseball-reference.com/allstar/2018-allstar-game.shtml
# https://www.mlb.com/gameday/al-all-stars-vs-nl-all-stars/2018/07/17/530856/live

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "extended_roster": True,
        "scorer": "Vicyorus",
        "date": "2018-07-17 20:23-23:57",
        "at": "Nationals Park, Washington, DC",
        "att": "43,843",
        "temp": "82F, Partly Cloudy",
        "wind": "6mph, In From CF",
        "away": {
            "team": "American League All-Stars",
            "starter": 519242,
            "roster": {
                # Lineup
                605141: {"jersey": 50, "name": "Mookie Betts"},  # BOS
                514888: {"jersey": 27, "name": "Jose Altuve"},  # HOU
                545361: {"jersey": 27, "name": "Mike Trout"},  # LAA
                502110: {"jersey": 28, "name": "J.D. Martinez"},  # BOS
                608070: {"jersey": 11, "name": "José Ramírez"},  # CLE
                592450: {"jersey": 99, "name": "Aaron Judge"},  # NYY
                592518: {"jersey": 13, "name": "Manny Machado"},  # BAL
                547989: {"jersey": 79, "name": "José Abreu"},  # CWS
                521692: {"jersey": 13, "name": "Salvador Perez"},  # KCR
                # Starting pitcher
                519242: {"jersey": 41, "name": "Chris Sale"},  # BOS
                # Bench
                516416: {"jersey": 2, "name": "Jean Segura"},  # SEA
                425783: {"jersey": 17, "name": "Shin-Soo Choo"},  # TEX
                571745: {"jersey": 17, "name": "Mitch Haniger"},  # SEA
                519048: {"jersey": 18, "name": "Mitch Moreland"},  # BOS
                608324: {"jersey": 2, "name": "Alex Bregman"},  # HOU
                476704: {"jersey": 8, "name": "Jed Lowrie"},  # OAK
                543228: {"jersey": 7, "name": "Yan Gomes"},  # CLE
                543807: {"jersey": 4, "name": "George Springer"},  # HOU
                488726: {"jersey": 23, "name": "Michael Brantley"},  # CLE
                596019: {"jersey": 12, "name": "Francisco Lindor"},  # CLE
                443558: {"jersey": 23, "name": "Nelson Cruz"},  # SEA
                # Bullpen
                622663: {"jersey": 40, "name": "Luis Severino"},  # NYY
                621244: {"jersey": 17, "name": "José Berríos"},  # MIN
                621242: {"jersey": 39, "name": "Edwin Díaz"},  # SEA
                518886: {"jersey": 46, "name": "Craig Kimbrel"},  # BOS
                605483: {"jersey": 4, "name": "Blake Snell"},  # TBR
                641729: {"jersey": 77, "name": "Joe Jiménez"},  # DET
                595014: {"jersey": 39, "name": "Blake Treinen"},  # OAK
                543037: {"jersey": 45, "name": "Gerrit Cole"},  # HOU
                457918: {"jersey": 33, "name": "J.A. Happ"},  # TOR
                450203: {"jersey": 50, "name": "Charlie Morton"},  # HOU
                545333: {"jersey": 47, "name": "Trevor Bauer"},  # CLE
            },
            "lefties": [519242, 605483, 457918],
            "lineup": [
                [605141, "9"],
                [514888, "4"],
                [545361, "8"],
                [502110, "0"],
                [608070, "5"],
                [592450, "7"],
                [592518, "6"],
                [547989, "3"],
                [521692, "2"],
            ],
            "bench": [
                [516416, "2B"],
                [425783, "RF"],
                [571745, "RF"],
                [519048, "1B"],
                [608324, "3B"],
                [476704, "SS"],
                [543228, "C"],
                [543807, "RF"],
                [488726, "DH"],
                [596019, "SS"],
                [443558, "DH"],
            ],
            "bullpen": [
                622663,
                621244,
                621242,
                518886,
                605483,
                641729,
                595014,
                543037,
                457918,
                450203,
                545333,
            ],
        },
        "home": {
            "team": "National League All-Stars",
            "starter": 453286,
            "roster": {
                # Lineup
                595879: {"jersey": 9, "name": "Javier Báez"},  # CHC
                571448: {"jersey": 28, "name": "Nolan Arenado"},  # COL
                502671: {"jersey": 44, "name": "Paul Goldschmidt"},  # ARI
                518692: {"jersey": 5, "name": "Freddie Freeman"},  # ATL
                461314: {"jersey": 27, "name": "Matt Kemp"},  # LAD
                547180: {"jersey": 34, "name": "Bryce Harper"},  # WSH
                455976: {"jersey": 22, "name": "Nick Markakis"},  # ATL
                543063: {"jersey": 35, "name": "Brandon Crawford"},  # SFG
                575929: {"jersey": 40, "name": "Willson Contreras"},  # CHC
                # Starting pitcher
                453286: {"jersey": 31, "name": "Max Scherzer"},  # WSH
                # Bench
                592663: {"jersey": 11, "name": "J.T. Realmuto"},  # MIA
                592885: {"jersey": 22, "name": "Christian Yelich"},  # MIL
                596115: {"jersey": 27, "name": "Trevor Story"},  # COL
                453568: {"jersey": 19, "name": "Charlie Blackmon"},  # COL
                456715: {"jersey": 6, "name": "Lorenzo Cain"},  # MIL
                458015: {"jersey": 19, "name": "Joey Votto"},  # CIN
                553993: {"jersey": 7, "name": "Eugenio Suárez"},  # CIN
                571697: {"jersey": 3, "name": "Scooter Gennett"},  # CIN
                645277: {"jersey": 1, "name": "Ozzie Albies"},  # ATL
                425877: {"jersey": 4, "name": "Yadier Molina"},  # STL
                542583: {"jersey": 24, "name": "Jesús Aguilar"},  # MIL
                # Bullpen
                425844: {"jersey": 21, "name": "Zack Greinke"},  # ARI
                623352: {"jersey": 71, "name": "Josh Hader"},  # MIL
                553878: {"jersey": 73, "name": "Felipe Vázquez"},  # PIT
                445276: {"jersey": 74, "name": "Kenley Jansen"},  # LAD
                592314: {"jersey": 26, "name": "Mike Foltynewicz"},  # ATL
                594798: {"jersey": 48, "name": "Jacob deGrom"},  # NYM
                571578: {"jersey": 46, "name": "Patrick Corbin"},  # ARI
                502026: {"jersey": 32, "name": "Jeremy Jeffress"},  # MIL
                548389: {"jersey": 22, "name": "Ross Stripling"},  # LAD
                605400: {"jersey": 27, "name": "Aaron Nola"},  # PHI
                543272: {"jersey": 52, "name": "Brad Hand"},  # SDP
            },
            "lefties": [623352, 553878, 571578, 543272],
            "lineup": [
                [595879, "4"],
                [571448, "5"],
                [502671, "0"],
                [518692, "3"],
                [461314, "7"],
                [547180, "8"],
                [455976, "9"],
                [543063, "6"],
                [575929, "2"],
            ],
            "bench": [
                [592663, "C"],
                [592885, "LF"],
                [596115, "SS"],
                [453568, "RF"],
                [456715, "CF"],
                [458015, "1B"],
                [553993, "3B"],
                [571697, "2B"],
                [645277, "2B"],
                [425877, "C"],
                [542583, "1B"],
            ],
            "bullpen": [
                425844,
                623352,
                553878,
                445276,
                592314,
                594798,
                571578,
                502026,
                548389,
                605400,
                543272,
            ],
        },
        "umpires": {
            "HP": "Ted Barrett",
            "1B": "Jim Reynolds",
            "2B": "Alfonso Márquez",
            "3B": "Andy Fletcher",
            "LF": "Mike Muchlinski",
            "RF": "Cory Blaser",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: NL #31 Max Scherzer
t1 = game.new_inning()

# 1. AL #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b f t b c")
t1.out("!K")

# 2. AL #27 Jose Altuve (X - X - X)
t1.new_ab()
t1.pitch_list("c s s")
t1.out("K")

# 3. AL #27 Mike Trout (X - X - X)
t1.new_ab()
t1.pitch_list("s b s b b f f b")
t1.reach("BB")
t1.advance(3, "28 1B")

# 4. AL #28 J.D. Martinez (X - X - 27)
t1.new_ab()
t1.hit(1)

# 5. AL #11 José Ramírez (27 - X - 28)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("P4")


# Bot 1st
# Pitching: AL #41 Chris Sale
b1 = game.new_inning()

# 1. NL #9  Javier Báez (X - X - X)
b1.new_ab()
b1.hit(1)

# 2. NL #28 Nolan Arenado (X - X - 9)
b1.new_ab()
b1.out("F7")

# 3. NL #44 Paul Goldschmidt (X - X - 9)
b1.new_ab()
b1.pitch_list("b c f s")
b1.out("K")

# 4. NL #5  Freddie Freeman (X - X - 9)
b1.new_ab()
b1.pitch_list("s d")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NL #31 Max Scherzer
t2 = game.new_inning()

# 6. AL #99 Aaron Judge (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(4)

# 7. AL #13 Manny Machado (X - X - X)
t2.new_ab()
t2.out("F7")

# 8. AL #79 José Abreu (X - X - X)
t2.new_ab()
t2.pitch_list("c s s")
t2.out("K")

# 9. AL #13 Salvador Perez (X - X - X)
t2.new_ab()
t2.pitch_list("b f s f f f s")
t2.out("K")


# Bot 2nd
# Pitching: AL #40 Luis Severino
b2 = game.new_inning()

# Pitching change (AL): #40 Luis Severino replaces #41 Chris Sale
b2.pitching_substitution(622663)

# 5. NL #27 Matt Kemp (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2)

# 6. NL #34 Bryce Harper (X - 27 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f c s")
b2.out("K")

# 7. NL #22 Nick Markakis (X - 27 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f b")
b2.out("F7")

# 8. NL #35 Brandon Crawford (X - 27 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("d c d b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NL #48 Jacob deGrom
t3 = game.new_inning()

# Pitching change (NL): #48 Jacob deGrom replaces #31 Max Scherzer
t3.pitching_substitution(594798)

# 1. AL #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("F8")

# 2. AL #27 Jose Altuve (X - X - X)
t3.new_ab()
t3.pitch_list("b s")
t3.out("P5")

# 3. AL #27 Mike Trout (X - X - X)
t3.new_ab()
t3.pitch_list("b f s")
t3.hit(4)

# 4. AL #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("b s b f s")
t3.out("K")


# Bot 3rd
# Pitching: AL #4  Blake Snell
b3 = game.new_inning()

# Pitching change (AL): #4  Blake Snell replaces #40 Luis Severino
b3.pitching_substitution(605483)

# 9. NL #40 Willson Contreras (X - X - X)
b3.new_ab()
b3.hit(4)

# 1. NL #9  Javier Báez (X - X - X)
b3.new_ab()
b3.pitch_list("f s b f b b")
b3.out("G1-3")

# 2. NL #28 Nolan Arenado (X - X - X)
b3.new_ab()
b3.pitch_list("c f b s")
b3.out("K2-3")

# 3. NL #44 Paul Goldschmidt (X - X - X)
b3.new_ab()
b3.pitch_list("f f b b b b")
b3.reach("BB")

# 4. NL #5  Freddie Freeman (X - X - 44)
b3.new_ab()
b3.pitch_list("b b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NL #26 Mike Foltynewicz
t4 = game.new_inning()

# Pitching change (NL): #26 Mike Foltynewicz replaces #48 Jacob deGrom
t4.pitching_substitution(592314)

# 5. AL #11 José Ramírez (X - X - X)
t4.new_ab()
t4.pitch_list("f c c")
t4.out("!K")

# 6. AL #99 Aaron Judge (X - X - X)
t4.new_ab()
t4.pitch_list("b b b s b")
t4.reach("BB")

# 7. AL #13 Manny Machado (X - X - 99)
t4.new_ab()
t4.pitch_list("f s 1 b b")
t4.out("P5")

# 8. AL #79 José Abreu (X - X - 99)
t4.new_ab()
t4.pitch_list("c s b")
t4.out("F8")


# Bot 4th
# Pitching: AL #4  Blake Snell
b4 = game.new_inning()

# 5. NL #27 Matt Kemp (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b f f c")
b4.out("!K")

# 6. NL #34 Bryce Harper (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s b c")
b4.out("!K")

# 7. NL #22 Nick Markakis (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c b")
b4.reach("BB")

# Pitching change (AL): #77 Joe Jiménez replaces #4  Blake Snell
b4.pitching_substitution(641729)

# 8. NL #35 Brandon Crawford (X - X - 22)
b4.new_ab()
b4.pitch_list("b c b s b f f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NL #27 Aaron Nola
t5 = game.new_inning()

# Pitching change (NL): #27 Aaron Nola replaces #26 Mike Foltynewicz
t5.pitching_substitution(605400)

# 9. AL #13 Salvador Perez (X - X - X)
t5.new_ab()
t5.pitch_list("f f b s")
t5.out("K")

# 1. AL #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("b b f f b f s")
t5.out("K")

# 2. AL #27 Jose Altuve (X - X - X)
t5.new_ab()
t5.hit(1)

# 3. AL #27 Mike Trout (X - X - 27)
t5.new_ab()
t5.pitch_list("c b")
t5.out("(F)P3")


# Bot 5th
# Pitching: AL #17 José Berríos
b5 = game.new_inning()

# Pitching change (AL): #17 José Berríos replaces #77 Joe Jiménez
b5.pitching_substitution(621244)

# 9. NL #40 Willson Contreras (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("G6-3")

# 1. NL #9  Javier Báez (X - X - X)
b5.new_ab()
b5.pitch_list("b f s b")
b5.out("F9")

# 2. NL #28 Nolan Arenado (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# Offensive change (NL): Pinch-hitter #4 Yadier Molina replaces #44 Paul Goldschmidt, batting 3rd
b5.offensive_substitution(3, 425877, "PH")

# 3. NL #4  Yadier Molina (X - X - 28)
b5.new_ab()
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NL #32 Jeremy Jeffress
t6 = game.new_inning()

# Pitching change (NL): #32 Jeremy Jeffress replaces #27 Aaron Nola
t6.pitching_substitution(502026)

# Defensive change (NL): #1 Ozzie Albies replaces #9 Javier Báez (2B), playing 2B, batting 1st
t6.defensive_substitution(1, 645277, "4")

# Defensive change (NL): #7 Eugenio Suárez replaces #28 Nolan Arenado (3B), playing 3B, batting 2nd
t6.defensive_substitution(2, 553993, "5")

# Defensive switch (NL): #4 Yadier Molina moves to DH
t6.defensive_switch(425877, "0")

# Defensive change (NL): #19 Joey Votto replaces #5 Freddie Freeman (1B), playing 1B, batting 4th
t6.defensive_substitution(4, 458015, "3")

# Defensive change (NL): #22 Christian Yelich replaces #27 Matt Kemp (LF), playing LF, batting 5th
t6.defensive_substitution(5, 592885, "7")

# Defensive change (NL): #19 Charlie Blackmon replaces #34 Bryce Harper (CF), playing CF, batting 6th
t6.defensive_substitution(6, 453568, "8")

# Defensive change (NL): #6 Lorenzo Cain replaces #22 Nick Markakis (RF), playing RF, batting 7th
t6.defensive_substitution(7, 456715, "9")

# Defensive change (NL): #27 Trevor Story replaces #35 Brandon Crawford (SS), playing SS, batting 8th
t6.defensive_substitution(8, 596115, "6")

# Defensive change (NL): #11 J.T. Realmuto replaces #40 Willson Contreras (C), playing C, batting 9th
t6.defensive_substitution(9, 592663, "2")

# Offensive change (AL): Pinch-hitter #23 Nelson Cruz replaces #28 J.D. Martinez, batting 4th
t6.offensive_substitution(4, 443558, "PH")

# 4. AL #23 Nelson Cruz (X - X - X)
t6.new_ab()
t6.pitch_list("b s b f f b f b")
t6.reach("BB")
t6.thrown_out(2, "2 FC6", 1, 502026)

# Offensive change (AL): Pinch-hitter #2 Alex Bregman replaces #11 José Ramírez, batting 5th
t6.offensive_substitution(5, 608324, "PH")

# 5. AL #2  Alex Bregman (X - X - 23)
t6.new_ab()
t6.pitch_list("c")
t6.reach("FC6")
t6.advance(2, "99 G5-3")

# 6. AL #99 Aaron Judge (X - X - 2)
t6.new_ab()
t6.pitch_list("c")
t6.out("G5-3")

# Offensive change (AL): Pinch-hitter #12 Francisco Lindor replaces #13 Manny Machado, batting 7th
t6.offensive_substitution(7, 596019, "PH")

# 7. AL #12 Francisco Lindor (X - 2 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b f")
t6.out("F8")


# Bot 6th
# Pitching: AL #39 Blake Treinen
b6 = game.new_inning()

# Pitching change (AL): #39 Blake Treinen replaces #17 José Berríos
b6.pitching_substitution(595014)

# Defensive change (AL): #17 Mitch Haniger replaces #27 Mike Trout (CF), playing RF, batting 3rd
b6.defensive_substitution(3, 571745, "9")

# Defensive change (AL): #8 Jed Lowrie replaces #27 Jose Altuve (2B), playing 2B, batting 2nd
b6.defensive_substitution(2, 476704, "4")

# Defensive change (AL): #4 George Springer replaces #99 Aaron Judge (LF), playing CF, batting 6th
b6.defensive_substitution(6, 543807, "8")

# Defensive switch (AL): #23 Nelson Cruz moves to DH
b6.defensive_switch(443558, "0")

# Defensive switch (AL): #2 Alex Bregman moves to 3B
b6.defensive_switch(608324, "5")

# Defensive change (AL): #23 Michael Brantley replaces #50 Mookie Betts (RF), playing LF, batting 1st
b6.defensive_substitution(1, 488726, "7")

# Defensive switch (AL): #12 Francisco Lindor moves to SS
b6.defensive_switch(596019, "6")

# Defensive change (AL): #7 Yan Gomes replaces #13 Salvador Perez (C), playing C, batting 9th
b6.defensive_substitution(9, 543228, "2")

# Defensive change (AL): #18 Mitch Moreland replaces #79 José Abreu (1B), playing 1B, batting 8th
b6.defensive_substitution(8, 519048, "3")

# 4. NL #19 Joey Votto (X - X - X)
b6.new_ab()
b6.pitch_list("c b s")
b6.out("F9")

# 5. NL #22 Christian Yelich (X - X - X)
b6.new_ab()
b6.pitch_list("f f f f f")
b6.out("G4-3")

# 6. NL #19 Charlie Blackmon (X - X - X)
b6.new_ab()
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NL #73 Felipe Vázquez
t7 = game.new_inning()

# Pitching change (NL): #73 Felipe Vázquez replaces #32 Jeremy Jeffress
t7.pitching_substitution(553878)

# 8. AL #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b s s f b b c")
t7.out("!K")

# 9. AL #7  Yan Gomes (X - X - X)
t7.new_ab()
t7.out("G5-3")

# 1. AL #23 Michael Brantley (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(2, "8 BB")

# 2. AL #8  Jed Lowrie (X - X - 23)
t7.new_ab()
t7.pitch_list("b b s f f b b")
t7.reach("BB")

# 3. AL #17 Mitch Haniger (X - 23 - 8)
t7.new_ab(is_risp=True)
t7.pitch_list("s c f b b c")
t7.out("!K")


# Bot 7th
# Pitching: AL #50 Charlie Morton
b7 = game.new_inning()

# Pitching change (AL): #50 Charlie Morton replaces #39 Blake Treinen
b7.pitching_substitution(450203)

# 7. NL #6  Lorenzo Cain (X - X - X)
b7.new_ab()
b7.out("L9")

# 8. NL #27 Trevor Story (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(4)

# 9. NL #11 J.T. Realmuto (X - X - X)
b7.new_ab()
b7.pitch_list("b s b b s f f f f b")
b7.reach("BB")
b7.advance(2, "1 G4-3")
b7.advance(3, "24 WP")

# 1. NL #1  Ozzie Albies (X - X - 11)
b7.new_ab()
b7.pitch_list("s c")
b7.out("G4-3")

# 2. NL #7  Eugenio Suárez (X - 11 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("f f")
b7.reach("HBP")
b7.advance(2, "24 WP")

# Offensive change (NL): Pinch-hitter #24 Jesús Aguilar replaces #4 Yadier Molina, batting 3rd
b7.offensive_substitution(3, 542583, "PH")

# 3. NL #24 Jesús Aguilar (X - 11 - 7)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b b")
b7.wp()
b7.out("P6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NL #71 Josh Hader
t8 = game.new_inning()

# Pitching change (NL): #71 Josh Hader replaces #73 Felipe Vázquez
t8.pitching_substitution(623352)

# Defensive switch (NL): #24 Jesús Aguilar moves to DH
t8.defensive_switch(542583, "0")

# Offensive change (AL): Pinch-hitter #17 Shin-Soo Choo replaces #23 Nelson Cruz, batting 4th
t8.offensive_substitution(4, 425783, "PH")

# 4. AL #17 Shin-Soo Choo (X - X - X)
t8.new_ab()
t8.pitch_list("b c c b")
t8.hit(1)
t8.advance(2, "4 1B")
t8.advance(4, "2 HR")

# 5. AL #2  Alex Bregman (X - X - 17)
t8.new_ab()
t8.pitch_list("b c c s")
t8.out("K")

# 6. AL #4  George Springer (X - X - 17)
t8.new_ab()
t8.pitch_list("c b b")
t8.hit(1)
t8.advance("U", "2 HR")

# Offensive change (AL): Pinch-hitter #2 Jean Segura replaces #12 Francisco Lindor, batting 7th
t8.offensive_substitution(7, 516416, "PH")

# 7. AL #2  Jean Segura (X - 17 - 4)
t8.new_ab(is_risp=True)
t8.pitch_list("s b b b f f f")
t8.error(3)
t8.hit("U", rbis=3)

# 8. AL #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b c b s")
t8.hit(1)

# Pitching change (NL): #52 Brad Hand replaces #71 Josh Hader
t8.pitching_substitution(543272)

# 9. AL #7  Yan Gomes (X - X - 18)
t8.new_ab()
t8.pitch_list("b c f s")
t8.out("K")

# 1. AL #23 Michael Brantley (X - X - 18)
t8.new_ab()
t8.pitch_list("f c b")
t8.out("G4-3")


# Bot 8th
# Pitching: AL #50 Charlie Morton
b8 = game.new_inning()

# Defensive switch (AL): #17 Shin-Soo Choo moves to DH
b8.defensive_switch(425783, "0")

# Defensive switch (AL): #2 Jean Segura moves to SS
b8.defensive_switch(516416, "6")

# 4. NL #19 Joey Votto (X - X - X)
b8.new_ab()
b8.pitch_list("b c b")
b8.out("G4-3")

# 5. NL #22 Christian Yelich (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.hit(4)

# 6. NL #19 Charlie Blackmon (X - X - X)
b8.new_ab()
b8.pitch_list("b f b c s")
b8.out("K")

# 7. NL #6  Lorenzo Cain (X - X - X)
b8.new_ab()
b8.pitch_list("s b c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NL #52 Brad Hand
t9 = game.new_inning()

# 2. AL #8  Jed Lowrie (X - X - X)
t9.new_ab()
t9.pitch_list("c b c")
t9.out("P3")

# Pitching change (NL): #22 Ross Stripling replaces #52 Brad Hand
t9.pitching_substitution(548389)

# 3. AL #17 Mitch Haniger (X - X - X)
t9.new_ab()
t9.pitch_list("b f b s b")
t9.out("G6-3")

# 4. AL #17 Shin-Soo Choo (X - X - X)
t9.new_ab()
t9.pitch_list("c s b f f f")
t9.out("G6-3")


# Bot 9th
# Pitching: AL #39 Edwin Díaz
b9 = game.new_inning()

# Pitching change (AL): #39 Edwin Díaz replaces #50 Charlie Morton
b9.pitching_substitution(621242)

# 8. NL #27 Trevor Story (X - X - X)
b9.new_ab()
b9.pitch_list("b f b b c f s")
b9.out("K")

# 9. NL #11 J.T. Realmuto (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
b9.advance(4, "3 HR")

# Offensive change (NL): Pinch-hitter #3 Scooter Gennett replaces #1 Ozzie Albies, batting 1st
b9.offensive_substitution(1, 571697, "PH")

# 1. NL #3  Scooter Gennett (X - X - 11)
b9.new_ab()
b9.pitch_list("b")
b9.hit(4, rbis=2)

# 2. NL #7  Eugenio Suárez (X - X - X)
b9.new_ab()
b9.pitch_list("f c b s")
b9.out("K")

# 3. NL #24 Jesús Aguilar (X - X - X)
b9.new_ab()
b9.pitch_list("c b s b")
b9.out("F8")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: NL #22 Ross Stripling
t10 = game.new_inning()

# Defensive switch (NL): #3 Scooter Gennett moves to 2B
t10.defensive_switch(571697, "4")

# 5. AL #2  Alex Bregman (X - X - X)
t10.new_ab()
t10.pitch_list("c b f b")
t10.hit(4)

# 6. AL #4  George Springer (X - X - X)
t10.new_ab()
t10.hit(4)

# 7. AL #2  Jean Segura (X - X - X)
t10.new_ab()
t10.pitch_list("c b b")
t10.hit(1)
t10.advance(3, "18 1B")
t10.advance(4, "23 SF7")

# 8. AL #18 Mitch Moreland (X - X - 2)
t10.new_ab()
t10.pitch_list("b c s f f")
t10.hit(1)

# 9. AL #7  Yan Gomes (2 - X - 18)
t10.new_ab(is_risp=True)
t10.pitch_list("c f s")
t10.out("K")

# 1. AL #23 Michael Brantley (2 - X - 18)
t10.new_ab(is_risp=True)
t10.out("SF7", rbis=1)

# 2. AL #8  Jed Lowrie (X - X - 18)
t10.new_ab()
t10.pitch_list("f b s f b")
t10.out("G3")


# Bot 10th
# Pitching: AL #33 J.A. Happ
b10 = game.new_inning()

# Pitching change (AL): #33 J.A. Happ replaces #39 Edwin Díaz
b10.pitching_substitution(457918)

# 4. NL #19 Joey Votto (X - X - X)
b10.new_ab()
b10.hit(4)

# 5. NL #22 Christian Yelich (X - X - X)
b10.new_ab()
b10.pitch_list("f c b s")
b10.out("K")

# 6. NL #19 Charlie Blackmon (X - X - X)
b10.new_ab()
b10.pitch_list("b c")
b10.out("G3")

# 7. NL #6  Lorenzo Cain (X - X - X)
b10.new_ab()
b10.pitch_list("c b s")
b10.out("F9")

# Winning team: AL
# WP: AL #39 Edwin Díaz
game.winning_pitcher(621242, is_away_team=True)
# SV: AL #33 J.A. Happ
game.save_pitcher(457918, is_away_team=True)

# Loser team: NL
# LP: NL #22 Ross Stripling
game.losing_pitcher(548389)

# print(game)
game.generate_scorecard()
