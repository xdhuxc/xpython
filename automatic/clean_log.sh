#!/usr/bin/env bash

# the script's log file
log_file="/var/log/yonyouclean-`date +%Y-%m-%d`.log"
touch ${log_file}

# author: xdhuxc
# time: 2018-03-31
# description：clean up logs of the docker containers on the current host. <--清理当前机器上的docker容器日志
#
function clean_container_log() {
    docker ps | awk 'NR > 1 {print $1}' | while read container_id
    do
        # get the container's name,including /. <--获取容器名称，包含/
        container_name=$(docker inspect --format={{.Name}} ${container_id})
        echo -e ${container_name:1}
        # get the container's log path. <--获取容器日志路径
        container_log_path=$(docker inspect --format={{.LogPath}} ${container_id})
        echo -e ${container_log_path}
        echo -e "$(date "+%Y-%m-%d %H:%M:%S") start to clean the container ${container_name:1}'s log." >> ${log_file} # 开始清理容器${container_name:1}的日志
        # clean up the container's log. <--清理容器日志
        echo "" > ${container_log_path}
        echo -e "$(date "+%Y-%m-%d %H:%M:%S") end up cleaning the container ${container_name:1}'s log." >> ${log_file} # 清理容器${container_name:1}的日志结束
    done
}

# author: xdhuxc
# time: 2018-03-31
# description：clean up non-running docker containers on the current host. <--清理非运行状态的docker容器
function clean_unused_container() {
    docker ps -a | awk 'NR > 1 {print $1}' | while read container_id
    do
        # get the container's name,including /. <--获取容器名称，包含/
        container_name=$(docker inspect --format={{.Name}} ${container_id})
        echo -e ${container_name:1}
        # get the container's status. <--获取容器当前状态
        container_status=docker inspect --format={{.State.Running}} ${container_id}
        echo -e "$(date "+%Y-%m-%d %H:%M:%S") start to clean the container ${container_name:1}." >> ${log_file} #
        # starting process
        if [ "${container_status}"x != "true"x ] ; then
            docker rm -f ${container_id}
        fi
        echo -e "$(date "+%Y-%m-%d %H:%M:%S") end up cleaning the container ${container_name:1}." >> ${log_file}
    done
}

# https://www.cnblogs.com/chen-lhx/p/6015421.html

# author: xdhuxc
# time: 2018-03-31
# description: clean the logs of user'application which are out of date.
# param1：the log directory, maybe contains subdirectory
function clear_log_outofdate_index() {
    root_dir=$1

}

clean_dir_log(){
    # -ctime    -n +n # 按文件创建时间来查找文件，-n指n天以内，+n指n天以前
    # -print 将查找到的文件输出到标准输出
    # {} \; 固定写法，一对大括号+空格+\
    # dir_name为绝对路径
    dir_name=$1
    before_days = $2
    find ${dir_name} -type f -ctime +${before_days} -exec rm -f {} \;
    # 分钟则为 -cmin
    # -size +512k 查找大于512k的文件
    # -size -512k 查找小于512k的文件
}



function main(){
    #
    clean_elasticsearch_outofdate_index es_user es_password es_host pattern
    echo -e "$(date "+%Y-%m-%d %H:%M:%S") start to clean elasticsearch indexes which are out of date." >> ${log_file} # 开始清理elasticsearch过期索引
    clean_elasticsearch_outofdate_index esadmin esadmin 172.20.15.42 developer_docker
    echo -e "$(date "+%Y-%m-%d %H:%M:%S") end up cleaning elasticsearch indexes which are out of date." >> ${log_file} # 清理elasticsearch过期索引结束

    echo -e "$(date "+%Y-%m-%d %H:%M:%S") start to clean docker container's log." >> ${log_file} # 开始清理docker容器日志
    clean_container_log
    echo -e "$(date "+%Y-%m-%d %H:%M:%S") end up cleaning docker container's log." >> ${log_file} # 清理docker容器日志结束

    echo -e "$(date "+%Y-%m-%d %H:%M:%S") start to clean non-running docker containers." >> ${log_file} # 开始清理非运行状态的docker容器
    clean_unused_container
     echo -e "$(date "+%Y-%m-%d %H:%M:%S") end up cleaning non-running docker containers." >> ${log_file} # 清理非运行状态的docker容器结束

}


main



