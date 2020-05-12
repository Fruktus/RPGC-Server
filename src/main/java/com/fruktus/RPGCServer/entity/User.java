package com.fruktus.RPGCServer.entity;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.UUID;

@Entity
@Table(name = "users")
@EqualsAndHashCode(of = {"id"})
public class User {
    @Id
    @Getter
    private UUID id;

    @Getter
    private String username;

    @Getter
    @Setter
    private String displayName;

    @Getter
    private int created_date;

    @Getter
    @Setter
    private String email;

    User(UUID id, String username){
        this.id = id;
        this.username = username;
        this.displayName = username;
        this.created_date = 0; // FIXME utc time now
    }

//    public static User fromAuthentication(Authentication authentication){
//        return PlayerInfo.fromAuthentication(authentication).getPlayer();
//    }
//
//    public static Player fromPrincipal(Principal principal){
//        return PlayerInfo.fromPrincipal(principal).getPlayer();
//    }

//    username = Column(String)  # non changeable
//    password = Column(String)
//    # check here: https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.encrypted.encrypted_type
//    created_date = Column(DateTime, default=datetime.datetime.utcnow)
//    email = Column(String)
//    rooms_owned = relationship('Room')
}
