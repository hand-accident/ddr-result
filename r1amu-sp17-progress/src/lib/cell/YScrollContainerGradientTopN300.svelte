<script>
    let className;
    export { className as class };
</script>

<div class="c {className}">
    <slot />
</div>

<style lang="postcss" module>
    .c {
        @apply container grow overflow-y-scroll bg-gradient-to-t from-neutral to-base-300 snap-y;
    }
</style>
