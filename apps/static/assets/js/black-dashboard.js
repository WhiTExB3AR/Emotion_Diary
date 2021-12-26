var transparent = true;
var transparentDemo = true;
var fixedTop = false;

var navbar_initialized = false;
var backgroundOrange = false;
var sidebar_mini_active = false;
var toggle_initialized = false;

var $html = $('html');
var $body = $('body');
var $navbar_minimize_fixed = $('.navbar-minimize-fixed');
var $collapse = $('.collapse');
var $navbar = $('.navbar');
var $tagsinput = $('.tagsinput');
var $selectpicker = $('.selectpicker');
var $navbar_color = $('.navbar[color-on-scroll]');
var $full_screen_map = $('.full-screen-map');
var $datetimepicker = $('.datetimepicker');
var $datepicker = $('.datepicker');
var $timepicker = $('.timepicker');

var seq = 0,
  delays = 80,
  durations = 500;
var seq2 = 0,
  delays2 = 80,
  durations2 = 500;

(function() {
  var isWindows = navigator.platform.indexOf('Win') > -1 ? true : false;

  if (isWindows) {
    // if we are on windows OS we activate the perfectScrollbar function
    if ($('.main-panel').length != 0) {
      var ps = new PerfectScrollbar('.main-panel', {
        wheelSpeed: 2,
        wheelPropagation: true,
        minScrollbarLength: 20,
        suppressScrollX: true
      });
    }

    if ($('.sidebar .sidebar-wrapper').length != 0) {

      var ps1 = new PerfectScrollbar('.sidebar .sidebar-wrapper');
      $('.table-responsive').each(function() {
        var ps2 = new PerfectScrollbar($(this)[0]);
      });
    }



    $html.addClass('perfect-scrollbar-on');
  } else {
    $html.addClass('perfect-scrollbar-off');
  }
})();

$(document).ready(function() {

  var scroll_start = 0;
  var startchange = $('.row');
  var offset = startchange.offset();
  var scrollElement = navigator.platform.indexOf('Win') > -1 ? $(".ps") : $(window);
  scrollElement.scroll(function() {

    scroll_start = $(this).scrollTop();

    if (scroll_start > 50) {
      $(".navbar-minimize-fixed").css('opacity', '1');
    } else {
      $(".navbar-minimize-fixed").css('opacity', '0');
    }
  });


  $(document).scroll(function() {
    scroll_start = $(this).scrollTop();
    if (scroll_start > offset.top) {
      $(".navbar-minimize-fixed").css('opacity', '1');
    } else {
      $(".navbar-minimize-fixed").css('opacity', '0');
    }
  });

  if ($('.full-screen-map').length == 0 && $('.bd-docs').length == 0) {
    // On click navbar-collapse the menu will be white not transparent
    $('.collapse').on('show.bs.collapse', function() {
      $(this).closest('.navbar').removeClass('navbar-transparent').addClass('bg-white');
    }).on('hide.bs.collapse', function() {
      $(this).closest('.navbar').addClass('navbar-transparent').removeClass('bg-white');
    });
  }

  blackDashboard.initMinimizeSidebar();

  $navbar = $('.navbar[color-on-scroll]');
  scroll_distance = $navbar.attr('color-on-scroll') || 500;

  // Check if we have the class "navbar-color-on-scroll" then add the function to remove the class "navbar-transparent" so it will transform to a plain color.
  if ($('.navbar[color-on-scroll]').length != 0) {
    blackDashboard.checkScrollForTransparentNavbar();
    $(window).on('scroll', blackDashboard.checkScrollForTransparentNavbar)
  }

  $('.form-control').on("focus", function() {
    $(this).parent('.input-group').addClass("input-group-focus");
  }).on("blur", function() {
    $(this).parent(".input-group").removeClass("input-group-focus");
  });

  // Activate bootstrapSwitch
  $('.bootstrap-switch').each(function() {
    $this = $(this);
    data_on_label = $this.data('on-label') || '';
    data_off_label = $this.data('off-label') || '';

    $this.bootstrapSwitch({
      onText: data_on_label,
      offText: data_off_label
    });
  });
});

$(document).on('click', '.navbar-toggle', function() {
  var $toggle = $(this);

  if (blackDashboard.misc.navbar_menu_visible == 1) {
    $html.removeClass('nav-open');
    blackDashboard.misc.navbar_menu_visible = 0;
    setTimeout(function() {
      $toggle.removeClass('toggled');
      $('.bodyClick').remove();
    }, 550);

  } else {
    setTimeout(function() {
      $toggle.addClass('toggled');
    }, 580);

    var div = '<div class="bodyClick"></div>';
    $(div).appendTo('body').click(function() {
      $html.removeClass('nav-open');
      blackDashboard.misc.navbar_menu_visible = 0;
      setTimeout(function() {
        $toggle.removeClass('toggled');
        $('.bodyClick').remove();
      }, 550);
    });

    $html.addClass('nav-open');
    blackDashboard.misc.navbar_menu_visible = 1;
  }
});

$(window).resize(function() {
  // reset the seq for charts drawing animations
  seq = seq2 = 0;

  if ($full_screen_map.length == 0 && $('.bd-docs').length == 0) {
    var isExpanded = $navbar.find('[data-toggle="collapse"]').attr("aria-expanded");
    if ($navbar.hasClass('bg-white') && $(window).width() > 991) {
      $navbar.removeClass('bg-white').addClass('navbar-transparent');
    } else if ($navbar.hasClass('navbar-transparent') && $(window).width() < 991 && isExpanded != "false") {
      $navbar.addClass('bg-white').removeClass('navbar-transparent');
    }
  }
});

blackDashboard = {
  misc: {
    navbar_menu_visible: 0
  },

  initMinimizeSidebar: function() {
    if ($('.sidebar-mini').length != 0) {
      sidebar_mini_active = true;
    }

    $('#minimizeSidebar').click(function() {
      var $btn = $(this);

      if (sidebar_mini_active == true) {
        $('body').removeClass('sidebar-mini');
        sidebar_mini_active = false;
        blackDashboard.showSidebarMessage('Sidebar mini deactivated...');
      } else {
        $('body').addClass('sidebar-mini');
        sidebar_mini_active = true;
        blackDashboard.showSidebarMessage('Sidebar mini activated...');
      }

      // we simulate the window Resize so the charts will get updated in realtime.
      var simulateWindowResize = setInterval(function() {
        window.dispatchEvent(new Event('resize'));
      }, 180);

      // we stop the simulation of Window Resize after the animations are completed
      setTimeout(function() {
        clearInterval(simulateWindowResize);
      }, 1000);
    });
  },

  showSidebarMessage: function(message) {
    try {
      $.notify({
        icon: "tim-icons ui-1_bell-53",
        message: message
      }, {
        type: 'info',
        timer: 4000,
        placement: {
          from: 'top',
          align: 'right'
        }
      });
    } catch (e) {
      console.log('Notify library is missing, please make sure you have the notifications library added.');
    }

  }

};

function hexToRGB(hex, alpha) {
  var r = parseInt(hex.slice(1, 3), 16),
    g = parseInt(hex.slice(3, 5), 16),
    b = parseInt(hex.slice(5, 7), 16);

  if (alpha) {
    return "rgba(" + r + ", " + g + ", " + b + ", " + alpha + ")";
  } else {
    return "rgb(" + r + ", " + g + ", " + b + ")";
  }
}

function floatchart() {
  // [ seo-card1 ] start
  $(function() {
      var options1 = {
          chart: {
              type: 'area',
              height: 145,
              sparkline: {
                  enabled: true
              }
          },
          dataLabels: {
              enabled: false
          },
          colors: ["#ff5370"],
          fill: {
              type: 'gradient',
              gradient: {
                  shade: 'dark',
                  gradientToColors: ['#ff869a'],
                  shadeIntensity: 1,
                  type: 'horizontal',
                  opacityFrom: 1,
                  opacityTo: 0.8,
                  stops: [0, 100, 100, 100]
              },
          },
          stroke: {
              curve: 'smooth',
              width: 2,
          },
          series: [{
              data: [45, 35, 60, 50, 85, 70]
          }],
          yaxis: {
             min: 5,
             max: 90,
         },
          tooltip: {
              fixed: {
                  enabled: false
              },
              x: {
                  show: false
              },
              y: {
                  title: {
                      formatter: function(seriesName) {
                          return 'Ticket '
                      }
                  }
              },
              marker: {
                  show: false
              }
          }
      }
      new ApexCharts(document.querySelector("#seo-card1"), options1).render();
  });
  // [ seo-card1 ] end
  // [ customer-chart ] start
  $(function() {
      var options = {
          chart: {
              height: 150,
              type: 'donut',
          },
          dataLabels: {
              enabled: false
          },
          plotOptions: {
              pie: {
                  donut: {
                      size: '75%'
                  }
              }
          },
          labels: ['New', 'Return'],
          series: [39, 10],
          legend: {
              show: false
          },
          tooltip: {
              theme: 'datk'
          },
          grid: {
              padding: {
                  top: 20,
                  right: 0,
                  bottom: 0,
                  left: 0
              },
          },
          colors: ["#4680ff", "#2ed8b6"],
          fill: {
              opacity: [1, 1]
          },
          stroke: {
              width: 0,
          }
      }
      var chart = new ApexCharts(document.querySelector("#customer-chart"), options);
      chart.render();
      var options1 = {
          chart: {
              height: 150,
              type: 'donut',
          },
          dataLabels: {
              enabled: false
          },
          plotOptions: {
              pie: {
                  donut: {
                      size: '75%'
                  }
              }
          },
          labels: ['New', 'Return'],
          series: [20, 15],
          legend: {
              show: false
          },
          tooltip: {
              theme: 'dark'
          },
          grid: {
              padding: {
                  top: 20,
                  right: 0,
                  bottom: 0,
                  left: 0
              },
          },
          colors: ["#fff", "#2ed8b6"],
          fill: {
              opacity: [1, 1]
          },
          stroke: {
              width: 0,
          }
      }
      var chart = new ApexCharts(document.querySelector("#customer-chart1"), options1);
      chart.render();
  });
  // [ customer-chart ] end
  // [ unique-visitor-chart ] start
  $(function() {
      var options = {
          chart: {
              height: 230,
              type: 'line',
              toolbar: {
                  show: false,
              },
          },
          dataLabels: {
              enabled: false
          },
          stroke: {
              width: 2,
              curve: 'smooth'
          },
          series: [{
              name: 'Arts',
              data: [20, 50, 30, 60, 30, 50]
          }, {
              name: 'Commerce',
              data: [60, 30, 65, 45, 67, 35]
          }],
          legend: {
              position: 'top',
          },
          xaxis: {
              type: 'datetime',
              categories: ['1/11/2000', '2/11/2000', '3/11/2000', '4/11/2000', '5/11/2000', '6/11/2000'],
              axisBorder: {
                  show: false,
              },
              label: {
                  style: {
                      color: '#ccc'
                  }
              },
          },
          yaxis: {
              show: true,
              min: 10,
              max: 70,
              labels: {
                  style: {
                      color: '#ccc'
                  }
              }
          },
          colors: ['#73b4ff', '#59e0c5'],
          fill: {
              type: 'gradient',
              gradient: {
                  shade: 'light',
                  gradientToColors: ['#4099ff', '#2ed8b6'],
                  shadeIntensity: 0.5,
                  type: 'horizontal',
                  opacityFrom: 1,
                  opacityTo: 1,
                  stops: [0, 100]
              },
          },
          markers: {
              size: 5,
              colors: ['#4099ff', '#2ed8b6'],
              opacity: 0.9,
              strokeWidth: 2,
              hover: {
                  size: 7,
              }
          },
          grid: {
              borderColor: '#cccccc3b',
          }
      }
      var chart = new ApexCharts(document.querySelector("#unique-visitor-chart"), options);
      chart.render();
  });
  // [ unique-visitor-chart ] end
}
