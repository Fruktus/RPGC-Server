//package com.fruktus.RPGCServer.component;
//
//@Component
//@RequiredArgsConstructor
//public class BasicAuth implements UserDetailsService{
//    private final PlayerInfoRepository playerInfoRepository;
//
//    @Override
//    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
//        return playerInfoRepository.findByPlayerUserName(username).orElseThrow(() -> new UsernameNotFoundException(username));
//    }
//}
