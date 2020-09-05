/*!
    * Start Bootstrap - SB Admin v6.0.1 (https://startbootstrap.com/templates/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
(function($) {
    "use strict";
    
    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
        $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
            if (this.href === path) {
                $(this).addClass("active");
            }
        });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });

    $("#submit_btn").click(function(){
        loadData();
    });
    
    var myLineChart;
    function initAreaChart(_labels, _data){
        // document.getElementById("myAreaChart").remove();
        if (myLineChart) {
            myLineChart.destroy();   
        }
        $("#myAreaChart").empty();
        var max_val = _data[0]
        $(_data).each(function(index, item){
            if (item > max_val){
                max_val = item
            }
        });
        var label_code = [];
        var label_name = [];
        $(_labels).each(function(index, item){
            label_code.push(item.productcode);
            label_name.push(item.productname);
        });
        // Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
        // Chart.defaults.global.defaultFontColor = '#292b2c';

        var ctx = document.getElementById("myAreaChart");
        myLineChart  = new Chart(ctx, {
            type: 'line',
            data: {
                labels: label_code,
                label_name:label_name,
                datasets: [{
                label: "评论数",
                lineTension: 0.3,
                backgroundColor: "rgba(2,117,216,0.2)",
                borderColor: "rgba(2,117,216,1)",
                pointRadius: 5,
                pointBackgroundColor: "rgba(2,117,216,1)",
                pointBorderColor: "rgba(255,255,255,0.8)",
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(2,117,216,1)",
                pointHitRadius: 50,
                pointBorderWidth: 2,
                data: _data,
                }],
            },
            options: {
                tooltips:{
                    callbacks: {
                        label: function(tooltipItem, data) {
                            console.info(data.datasets[0])
                            var label = data.label_name[tooltipItem.index] + " : " + data.datasets[0].data[tooltipItem.index] + "条";
                            return label;
                        }
                    }
                },
                scales: {
                    xAxes: [{
                        gridLines: {
                            display: false
                        },
                        ticks: {
                            maxTicksLimit: 7
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            min: 0,
                            max: max_val,
                            maxTicksLimit: 2
                        },
                        gridLines: {
                            color: "rgba(0, 0, 0, .125)",
                        }
                    }],
                },
                legend: {
                    display: false
                }
            }
        });
    }

    var myBarChart;
    function initBarChart(_labels, _data1, _data2){
        if (myBarChart) {
            myBarChart.destroy();   
        }
        // document.getElementById("myBarChart").remove();
        $("#myBarChart").empty();
        var max_val = _data1[0]
        
        $(_data1).each(function(index, item){
            if (item > max_val){
                max_val = item
            }
        });
        $(_data2).each(function(index, item){
            if (item > max_val){
                max_val = item
            }
        });
        var label_code = [];
        var label_name = [];
        console.info(_labels)
        $(_labels).each(function(index, item){
            label_code.push(item.productcode);
            label_name.push(item.productname);
        });
        // Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
        // Chart.defaults.global.defaultFontColor = '#292b2c';
        var ctx = document.getElementById("myBarChart");
        // console.info(_data1)
        // console.info(_data2)
        myBarChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: label_code,
                label_name:label_name,
                datasets: [{
                    label: "正向评论数",
                    backgroundColor: "rgba(220,220,220,1)",
                    borderColor: "rgba(220,220,220,0.2)",
                    data: _data1,
                },{
                    label: "负向评论数",
                    backgroundColor: "rgba(151,187,205,1)",
                    borderColor: "rgba(151,187,205,0.2)",
                    data: _data2,
                    }
                ],
            },
            options: {
                tooltips:{
                    callbacks: {
                        label: function(tooltipItem, data) {
                            console.info(data.datasets[0])
                            var label = data.label_name[tooltipItem.index] + "正向评价: " + data.datasets[0].data[tooltipItem.index] + "条\n\r";
                            label += data.label_name[tooltipItem.index] + "负向评价: " + data.datasets[1].data[tooltipItem.index] + "条";
                            return label;
                        }
                    }
                },
                scales: {
                    xAxes: [{
                        gridLines: {
                            display: false
                        },
                        ticks: {
                            maxTicksLimit: 6
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            min: 0,
                            max: max_val,
                            maxTicksLimit: 2
                        },
                        gridLines: {
                            display: true
                        }
                    }],
                },
                legend: {
                    display: false
                }
            }
        });
    }

    function loadData(){
        $.ajax({
            url:"/queryStatistic",
            type:"GET",
            data:{"productName":$("#p_name").val(), "productWords":$("#p_words").val(), "productTime":$("#p_time").val()},
            success:function(data){
                $("#total").html(data.total);
                $("#main").html(data.main);
                $("#pos").html(data.pos);
                $("#neg").html(data.neg);
            },
            error: function (jqXHR, textStatus, err) {
                console.log(arguments);
            }
        });

        $.ajax({
            url:"/queryAreaChart",
            type:"GET",
            data:{"productName":$("#p_name").val(), "productWords":$("#p_words").val(), "productTime":$("#p_time").val()},
            success:function(data){
                // console.log(data)
                initAreaChart(data.labels, data.vals);
            },
            error: function (jqXHR, textStatus, err) {
                console.log(arguments);
            }
        });

        $.ajax({
            url:"/queryBarChart",
            type:"GET",
            data:{"productName":$("#p_name").val(), "productWords":$("#p_words").val(), "productTime":$("#p_time").val()},
            success:function(data){
                initBarChart(data.labels, data.vals1, data.vals2);
            },
            error: function (jqXHR, textStatus, err) {
                console.log(arguments);
            }
        });

        $.ajax({
            url:"/queryDetails",
            type:"GET",
            data:{"productName":$("#p_name").val(), "productWords":$("#p_words").val(), "productTime":$("#p_time").val()},
            success:function(data){
                var content = "";
                $(data.ret_list).each(function(index, item){
                    // console.info(item);
                    content += "<tr><td>"+item.username+"</td><td>"+item.comments+"</td><td>"+(item.sentiments=="1"?"正向评价":"负向评价")+"</td><td>"+item.commenttime+"</td></tr>"
                });
                $("#tableBody").html(content);
            },
            error: function (jqXHR, textStatus, err) {
                console.log(arguments);
            }
        });

        if ($("#p_name").val()) {
            $("#product_name").html($("#p_name").val());
        }

    }
    loadData();
})(jQuery);

// $("#submit_btn").click();